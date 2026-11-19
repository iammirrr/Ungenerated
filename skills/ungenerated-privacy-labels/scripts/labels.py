#!/usr/bin/env python3
"""The App Privacy answer sheet from the privacy manifests an app actually ships.

Reads the app's own PrivacyInfo.xcprivacy files and every SDK's (Swift packages in DerivedData, CocoaPods, vendored
frameworks), merges them by data type and prints one row per type: purposes, linked, tracking, who declares it.
A type an SDK declares that the app's own manifest doesn't is marked MISSING: decide it, don't drop it.

  python3 labels.py <app repo> [--name <Xcode project name>]   # --name finds its DerivedData checkouts
  python3 labels.py --selftest
"""
import glob, os, plistlib, sys, tempfile

SKIP = ("/Tests/", "/Examples/", "/Example/", "/TestingApps/", "/Demo/", "/Samples/")
PURPOSE = {"AppFunctionality": "App Functionality", "Analytics": "Analytics", "ProductPersonalization": "Product Personalization",
           "DeveloperAdvertising": "Developer's Advertising or Marketing", "ThirdPartyAdvertising": "Third-Party Advertising", "Other": "Other Purposes"}


def manifests(repo, name=None):
    roots = [repo]
    if name:
        roots += glob.glob(os.path.expanduser(f"~/Library/Developer/Xcode/DerivedData/{name}-*/SourcePackages/checkouts"))
    for root in roots:
        for top, dirs, files in os.walk(root):  # never follows symlinks; skips heavy trees
            dirs[:] = [d for d in dirs if d not in (".git", "node_modules", "build", "DerivedData", ".build")]
            path = os.path.join(top, "PrivacyInfo.xcprivacy")
            if "PrivacyInfo.xcprivacy" in files and not any(s in path + "/" for s in SKIP):
                yield path, root == repo and "/Pods/" not in path


def merge(paths):
    rows = {}
    for path, own in paths:
        with open(path, "rb") as f:
            data = plistlib.load(f)
        who = "app" if own else path.split("/checkouts/")[-1].split("/")[0] if "/checkouts/" in path else os.path.basename(os.path.dirname(path))
        for t in data.get("NSPrivacyCollectedDataTypes", []):
            kind = t["NSPrivacyCollectedDataType"].replace("NSPrivacyCollectedDataType", "")
            r = rows.setdefault(kind, {"purposes": set(), "linked": False, "tracking": False, "who": set(), "app": False})
            r["purposes"] |= {p.replace("NSPrivacyCollectedDataTypePurpose", "") for p in t.get("NSPrivacyCollectedDataTypePurposes", [])}
            r["linked"] |= bool(t.get("NSPrivacyCollectedDataTypeLinked"))
            r["tracking"] |= bool(t.get("NSPrivacyCollectedDataTypeTracking"))
            r["who"].add(who)
            r["app"] |= own
    return rows


def table(rows):
    out = ["| Data type | Purposes | Linked | Tracking | Declared by |", "|---|---|---|---|---|"]
    for kind, r in sorted(rows.items()):
        flag = "" if r["app"] else " **MISSING from the app's manifest**"
        purposes = " + ".join(PURPOSE.get(p, p) for p in sorted(r["purposes"]))
        out.append(f"| {kind} | {purposes} | {'Yes' if r['linked'] else 'No'} | {'Yes' if r['tracking'] else 'No'} | {', '.join(sorted(r['who']))}{flag} |")
    return "\n".join(out)


def selftest():
    def plist(path, kind, linked, purpose):
        os.makedirs(os.path.dirname(path), exist_ok=True)
        with open(path, "wb") as f:
            plistlib.dump({"NSPrivacyCollectedDataTypes": [{"NSPrivacyCollectedDataType": "NSPrivacyCollectedDataType" + kind,
                "NSPrivacyCollectedDataTypeLinked": linked, "NSPrivacyCollectedDataTypeTracking": False,
                "NSPrivacyCollectedDataTypePurposes": ["NSPrivacyCollectedDataTypePurpose" + purpose]}]}, f)
    with tempfile.TemporaryDirectory() as d:
        plist(f"{d}/App/PrivacyInfo.xcprivacy", "CrashData", True, "AppFunctionality")
        plist(f"{d}/Pods/Sentry/PrivacyInfo.xcprivacy", "OtherDiagnosticData", False, "AppFunctionality")
        plist(f"{d}/Pods/Sentry/Tests/PrivacyInfo.xcprivacy", "Health", False, "Other")
        rows = merge(manifests(d))
    assert set(rows) == {"CrashData", "OtherDiagnosticData"}, rows   # test apps are skipped
    assert rows["CrashData"]["app"] and rows["CrashData"]["linked"]
    assert not rows["OtherDiagnosticData"]["app"] and "MISSING" in table(rows)
    print("selftest ok")


if __name__ == "__main__":
    args = sys.argv[1:]
    if args[:1] == ["--selftest"]:
        selftest()
    elif args:
        name = args[args.index("--name") + 1] if "--name" in args else None
        print(table(merge(manifests(os.path.abspath(args[0]), name))))
    else:
        print(__doc__)
