import os
import re

KERNEL_DIR = "."

def fix_ksud():
    path = os.path.join(KERNEL_DIR, "drivers/kernelsu/runtime/ksud.c")
    with open(path, "r") as f:
        content = f.read()
    if '#include "feature/selinux_hide.h"' not in content:
        content = content.replace(
            '#include "runtime/ksud.h"',
            '#include "runtime/ksud.h"\n#include "feature/selinux_hide.h"'
        )
    with open(path, "w") as f:
        f.write(content)
    print("Fixed ksud.c")

def fix_dispatch():
    path = os.path.join(KERNEL_DIR, "drivers/kernelsu/supercall/dispatch.c")
    with open(path, "r") as f:
        content = f.read()

    content = content.replace(
        "#ifdef CONFIG_KSU_SUSFS\n            susfs_start_sdcard_monitor_fn();\n#endif",
        ""
    )

    content = content.replace(
        """#ifdef CONFIG_KSU_SUSFS_SUS_MOUNT
         case CMD_SUSFS_HIDE_SUS_MNTS_FOR_NON_SU_PROCS:
            susfs_set_hide_sus_mnts_for_non_su_procs(arg);
            return 0;
#endif""",
        """#ifdef CONFIG_KSU_SUSFS_SUS_MOUNT
         case CMD_SUSFS_HIDE_SUS_MNTS_FOR_NON_SU_PROCS:
            return 0;
#endif"""
    )

    content = content.replace(
        """case CMD_SUSFS_ADD_SUS_PATH_LOOP:
            susfs_add_sus_path_loop(arg);
            return 0;""",
        """case CMD_SUSFS_ADD_SUS_PATH_LOOP:
            return 0;"""
    )

    content = content.replace(
        "susfs_add_sus_map(arg);",
        "susfs_add_sus_maps((struct st_susfs_sus_maps __user *)*arg);"
    )

    content = content.replace(
        """case CMD_SUSFS_ENABLE_AVC_LOG_SPOOFING:
            susfs_set_avc_log_spoofing(arg);
            return 0;""",
        """case CMD_SUSFS_ENABLE_AVC_LOG_SPOOFING:
            return 0;"""
    )

    content = content.replace(
        """case CMD_SUSFS_SHOW_ENABLED_FEATURES:
            susfs_get_enabled_features(arg);
            return 0;""",
        """case CMD_SUSFS_SHOW_ENABLED_FEATURES:
            return 0;"""
    )

    content = content.replace(
        """case CMD_SUSFS_SHOW_VARIANT:
            susfs_show_variant(arg);
            return 0;""",
        """case CMD_SUSFS_SHOW_VARIANT:
            return 0;"""
    )

    content = content.replace(
        """case CMD_SUSFS_SHOW_VERSION:
            susfs_show_version(arg);
            return 0;""",
        """case CMD_SUSFS_SHOW_VERSION:
            return 0;"""
    )

    content = content.replace(
        "susfs_set_cmdline_or_bootconfig(arg);",
        "susfs_set_cmdline_or_bootconfig((char __user *)*arg);"
    )

    content = content.replace(
        "susfs_add_open_redirect(arg);",
        "susfs_add_open_redirect((void __user *)*arg);"
    )

    content = content.replace(
        "susfs_add_sus_kstat(arg);",
        "susfs_add_sus_kstat((struct st_susfs_sus_kstat __user *)*arg);"
    )

    content = content.replace(
        "susfs_update_sus_kstat(arg);",
        "susfs_update_sus_kstat((struct st_susfs_sus_kstat __user *)*arg);"
    )

    content = content.replace(
        "susfs_set_uname(arg);",
        "susfs_set_uname((struct st_susfs_uname __user *)*arg);"
    )

    with open(path, "w") as f:
        f.write(content)
    print("Fixed dispatch.c")

def fix_adb_root():
    path = os.path.join(KERNEL_DIR, "drivers/kernelsu/feature/adb_root.c")
    with open(path, "r") as f:
        content = f.read()

    content = content.replace(
        """    return (susfs_starts_with(filename, "/apex/") &&
                susfs_ends_with(filename, "/adbd"));""",
        """    return (strstr(filename, "/apex/") == filename &&
                strstr(filename, "/adbd") != NULL);"""
    )

    with open(path, "w") as f:
        f.write(content)
    print("Fixed adb_root.c")

if __name__ == "__main__":
    fix_ksud()
    fix_dispatch()
    fix_adb_root()
    print("All fixes applied!")
