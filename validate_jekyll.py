#!/usr/bin/env python3
"""
ChristIAM- Jekyll Structure Validator
Validates config, front matter, layouts, Liquid tags, Sass imports, includes, and posts.

Usage: python3 validate_jekyll.py [project_root]
"""

import os
import re
import sys
import yaml

# ---- Helpers ----

def has_front_matter(content):
    """Check if file has valid Jekyll front matter (including empty)."""
    return bool(re.match(r"^---[\s\S]*?---", content))

def parse_front_matter(content):
    """Parse YAML front matter from file content. Returns dict or None."""
    fm_match = re.match(r"^---\n(.*?)\n---", content, re.DOTALL)
    if fm_match:
        try:
            return yaml.safe_load(fm_match.group(1))
        except Exception:
            return None
    return None


def main():
    project_root = sys.argv[1] if len(sys.argv) > 1 else "."
    os.chdir(project_root)

    errors = []
    passed_count = 0

    # ---- 1. _config.yml ----
    print("=" * 55)
    print("1. VALIDATING _config.yml")
    print("=" * 55)
    try:
        with open("_config.yml") as f:
            config = yaml.safe_load(f)
        required_keys = ["title", "description", "url", "baseurl"]
        for key in required_keys:
            if key in config:
                print(f"  ✓ config.{key} = {config[key]}")
                passed_count += 1
            else:
                errors.append(f"  ✗ Missing required key: {key}")
        if "plugins" in config:
            print(f"  ✓ plugins: {config['plugins']}")
            passed_count += 1
        if "defaults" in config:
            print(f"  ✓ defaults configured ({len(config['defaults'])} scopes)")
            passed_count += 1
    except Exception as e:
        errors.append(f"  ✗ _config.yml parse error: {e}")

    # ---- 2. Front matter ----
    print("\n" + "=" * 55)
    print("2. VALIDATING FRONT MATTER")
    print("=" * 55)
    md_files = []
    excluded = config.get("exclude", []) if isinstance(config, dict) else []
    for root, dirs, files in os.walk("."):
        if ".git" in root:
            continue
        for fn in files:
            if fn.endswith(".md"):
                rel = os.path.relpath(os.path.join(root, fn), ".")
                if rel in excluded:
                    continue
                md_files.append(rel)

    for fpath in sorted(md_files):
        with open(fpath) as f:
            content = f.read()
        if has_front_matter(content):
            fm = parse_front_matter(content) or {}
            layout = fm.get("layout", "N/A")
            title = fm.get("title", "N/A")
            print(f"  ✓ {fpath} — layout: {layout}, title: {title}")
            passed_count += 1
        else:
            errors.append(f"  ✗ {fpath} — missing front matter")

    # ---- 3. Layout references ----
    print("\n" + "=" * 55)
    print("3. VALIDATING LAYOUT REFERENCES")
    print("=" * 55)
    layouts_available = {
        fn.replace(".html", "")
        for fn in os.listdir("_layouts")
        if fn.endswith(".html")
    }
    print(f"  Available layouts: {sorted(layouts_available)}")

    for fpath in sorted(md_files):
        with open(fpath) as f:
            content = f.read()
        fm = parse_front_matter(content)
        if fm and "layout" in fm:
            layout = fm["layout"]
            if layout in layouts_available:
                print(f"  ✓ {fpath} → layout '{layout}'")
                passed_count += 1
            else:
                errors.append(f"  ✗ {fpath} → layout '{layout}' NOT FOUND")

    # Check layout-to-layout inheritance
    for fn in sorted(os.listdir("_layouts")):
        fpath = f"_layouts/{fn}"
        with open(fpath) as f:
            content = f.read()
        fm = parse_front_matter(content)
        if fm and "layout" in fm:
            parent = fm["layout"]
            if parent in layouts_available:
                print(f"  ✓ {fpath} → extends '{parent}'")
                passed_count += 1
            else:
                errors.append(f"  ✗ {fpath} → extends '{parent}' NOT FOUND")

    # ---- 4. Liquid tag balance ----
    print("\n" + "=" * 55)
    print("4. VALIDATING LIQUID TEMPLATE TAGS")
    print("=" * 55)
    template_files = []
    for root, dirs, files in os.walk("."):
        if ".git" in root:
            continue
        for fn in files:
            if fn.endswith((".html", ".md", ".scss")):
                rel = os.path.relpath(os.path.join(root, fn), ".")
                template_files.append(rel)

    for fpath in sorted(template_files):
        with open(fpath) as f:
            content = f.read()
        open_tags = len(re.findall(r"{%\s", content))
        close_tags = len(re.findall(r"\s%}", content))
        open_vars = len(re.findall(r"{{\s", content))
        close_vars = len(re.findall(r"\s}}", content))
        total = open_tags + open_vars
        if open_tags == close_tags and open_vars == close_vars:
            if total > 0:
                print(f"  ✓ {fpath} — {open_tags} Liquid, {open_vars} variables — balanced")
                passed_count += 1
        else:
            errors.append(
                f"  ✗ {fpath} — unbalanced (Liquid: {open_tags}/{close_tags}, vars: {open_vars}/{close_vars})"
            )

    # ---- 5. Sass imports ----
    print("\n" + "=" * 55)
    print("5. VALIDATING SASS IMPORTS")
    print("=" * 55)
    scss_path = "assets/css/main.scss"
    if os.path.exists(scss_path):
        with open(scss_path) as f:
            scss_content = f.read()

        # Check front matter (handles empty front matter correctly)
        if has_front_matter(scss_content):
            print(f"  ✓ {scss_path} has valid front matter")
            passed_count += 1
        else:
            errors.append(f"  ✗ {scss_path} missing front matter")

        imports = re.findall(r'@import\s+"([^"]+)"', scss_content)
        sass_files = {
            f for f in os.listdir("_sass") if f.endswith(".scss")
        }
        print(f"  Available Sass partials: {sorted(sass_files)}")
        for imp in imports:
            expected = f"_{imp}.scss"
            if expected in sass_files:
                print(f"  ✓ @import \"{imp}\" → {expected}")
                passed_count += 1
            else:
                errors.append(f"  ✗ @import \"{imp}\" → {expected} NOT FOUND")
    else:
        errors.append(f"  ✗ {scss_path} not found")

    # Also check any other .scss files for front matter
    for root, dirs, files in os.walk("assets"):
        if ".git" in root:
            continue
        for fn in files:
            if fn.endswith(".scss") and fn != "main.scss":
                rel = os.path.relpath(os.path.join(root, fn), ".")
                with open(rel) as f:
                    content = f.read()
                if has_front_matter(content):
                    print(f"  ✓ {rel} has valid front matter")
                    passed_count += 1
                else:
                    errors.append(f"  ✗ {rel} missing front matter")

    # ---- 6. Include references ----
    print("\n" + "=" * 55)
    print("6. VALIDATING INCLUDE REFERENCES")
    print("=" * 55)
    includes_available = set(os.listdir("_includes"))
    print(f"  Available includes: {sorted(includes_available)}")

    for fpath in sorted(template_files):
        with open(fpath) as f:
            content = f.read()
        include_refs = re.findall(r"{%\s*include\s+(\S+)\s*%}", content)
        for inc in include_refs:
            if inc in includes_available:
                print(f"  ✓ {fpath} → include '{inc}'")
                passed_count += 1
            else:
                errors.append(f"  ✗ {fpath} → include '{inc}' NOT FOUND")

    # ---- 7. Required files ----
    print("\n" + "=" * 55)
    print("7. CHECKING REQUIRED FILES")
    print("=" * 55)
    required = [
        "_config.yml", "Gemfile", "index.md", "README.md", "LICENSE",
        "_layouts/default.html", "_layouts/home.html", "_layouts/post.html",
        "_includes/head.html", "_includes/header.html",
        "_includes/footer.html", "_includes/scripts.html",
        "assets/css/main.scss", "assets/js/main.js", ".gitignore",
    ]
    for f in required:
        if os.path.exists(f):
            print(f"  ✓ {f}")
            passed_count += 1
        else:
            errors.append(f"  ✗ Missing required file: {f}")

    # ---- 8. Posts naming convention ----
    print("\n" + "=" * 55)
    print("8. VALIDATING POSTS NAMING")
    print("=" * 55)
    post_pattern = re.compile(r"^\d{4}-\d{2}-\d{2}-.+\.md$")
    if os.path.isdir("_posts"):
        for fn in sorted(os.listdir("_posts")):
            if post_pattern.match(fn):
                print(f"  ✓ _posts/{fn}")
                passed_count += 1
            else:
                errors.append(
                    f"  ✗ _posts/{fn} — invalid naming (expected YYYY-MM-DD-title.md)"
                )

    # ---- Summary ----
    print("\n" + "=" * 55)
    print("VALIDATION SUMMARY")
    print("=" * 55)
    print(f"  Checks passed: {passed_count}")
    print(f"  Errors:        {len(errors)}")
    if errors:
        print(f"\n  ❌ {len(errors)} ERROR(S):")
        for e in errors:
            print(f"     {e}")
        print(f"\n  🔴 {len(errors)} error(s) need to be fixed before building")
        sys.exit(1)
    else:
        print(f"\n  ✅ ALL {passed_count} CHECKS PASSED — Jekyll structure is valid and ready to build")
        sys.exit(0)


if __name__ == "__main__":
    main()
