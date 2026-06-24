import os
import re

KERNEL_DIR = "kernel"

def fix_ksud():
    path = os.path.join(KERNEL_DIR, "drivers/kernelsu/runtime/ksud.c")
    with open(path, "r") as f:
        content = f.read()
    # Add include for selinux_hide.h at the top
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
    
    # 1. Remove susfs_start_sdcard_monitor_fn call
    content = content.replace(
        "#ifdef CONFIG_KSU_SUSFS\n            susfs_start_sdcard_monitor_fn();\n#endif",
        ""
    )
    
    # 2. Replace CMD_SUSFS_HIDE_SUS_MNTS_FOR_NON_SU_PROCS case
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
    
    # 3. Replace CMD_SUSFS_ADD_SUS_PATH_LOOP case
    content = content.replace(
        """case CMD_SUSFS_ADD_SUS_PATH_LOOP:
            susfs_add_sus_path_loop(arg);
            return 0;""",
        """case CMD_SUSFS_ADD_SUS_PATH_LOOP:
            return 0;"""
    )
    
    # 4. Fix susfs_add_sus_map -> susfs_add_sus_maps with correct type
    content = content.replace(
        "susfs_add_sus_map(arg);",
        "susfs_add_sus_maps((struct st_susfs_sus_maps __user *)*arg);"
    )
    
    # 5. Replace CMD_SUSFS_ENABLE_AVC_LOG_SPOOFING case
    content = content.replace(
        """case CMD_SUSFS_ENABLE_AVC_LOG_SPOOFING:
            susfs_set_avc_log_spoofing(arg);
            return 0;""",
        """case CMD_SUSFS_ENABLE_AVC_LOG_SPOOFING:
            return 0;"""
    )
    
    # 6. Replace CMD_SUSFS_SHOW_ENABLED_FEATURES case
    content = content.replace(
        """case CMD_SUSFS_SHOW_ENABLED_FEATURES:
            susfs_get_enabled_features(arg);
            return 0;""",
        """case CMD_SUSFS_SHOW_ENABLED_FEATURES:
            return 0;"""
    )
    
    # 7. Replace CMD_SUSFS_SHOW_VARIANT case
    content = content.replace(
        """case CMD_SUSFS_SHOW_VARIANT:
            susfs_show_variant(arg);
            return 0;""",
        """case CMD_SUSFS_SHOW_VARIANT:
            return 0;"""
    )
    
    # 8. Replace CMD_SUSFS_SHOW_VERSION case
    content = content.replace(
        """case CMD_SUSFS_SHOW_VERSION:
            susfs_show_version(arg);
            return 0;""",
        """case CMD_SUSFS_SHOW_VERSION:
            return 0;"""
    )
    
    # 9. Fix susfs_set_cmdline_or_bootconfig signature
    content = content.replace(
        "susfs_set_cmdline_or_bootconfig(arg);",
        "susfs_set_cmdline_or_bootconfig((char __user *)*arg);"
    )
    
    # 10. Fix susfs_add_open_redirect -> not in susfs4ksu, stub it
    content = content.replace(
        "susfs_add_open_redirect(arg);",
        "susfs_add_open_redirect((void __user *)*arg);  // stub"
    )
    
    # 11. Fix susfs_add_sus_kstat signature
    content = content.replace(
        "susfs_add_sus_kstat(arg);",
        "susfs_add_sus_kstat((struct st_susfs_sus_kstat __user *)*arg);"
    )
    
    # 12. Fix susfs_set_uname signature
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
    
    # Replace susfs_starts_with/ends_with with simple string checks
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
