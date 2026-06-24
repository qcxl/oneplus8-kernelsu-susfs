#ifndef __SUSFS_COMPAT_H
#define __SUSFS_COMPAT_H

#include <linux/susfs.h>

/* SUSFS magic number for supercall */
#ifndef SUSFS_MAGIC
#define SUSFS_MAGIC 0xFAFAFAFA
#endif

/* Missing CMD constants */
#ifndef CMD_SUSFS_HIDE_SUS_MNTS_FOR_NON_SU_PROCS
#define CMD_SUSFS_HIDE_SUS_MNTS_FOR_NON_SU_PROCS 0x55557
#endif
#ifndef CMD_SUSFS_ADD_SUS_PATH_LOOP
#define CMD_SUSFS_ADD_SUS_PATH_LOOP 0x55553
#endif
#ifndef CMD_SUSFS_ADD_SUS_MAP
#define CMD_SUSFS_ADD_SUS_MAP 0x60020
#endif
#ifndef CMD_SUSFS_ENABLE_AVC_LOG_SPOOFING
#define CMD_SUSFS_ENABLE_AVC_LOG_SPOOFING 0x60010
#endif
#ifndef CMD_SUSFS_SHOW_ENABLED_FEATURES
#define CMD_SUSFS_SHOW_ENABLED_FEATURES 0x555e2
#endif
#ifndef CMD_SUSFS_SHOW_VARIANT
#define CMD_SUSFS_SHOW_VARIANT 0x555e3
#endif
#ifndef CMD_SUSFS_SHOW_VERSION
#define CMD_SUSFS_SHOW_VERSION 0x555e1
#endif
#ifndef CMD_SUSFS_SET_CMDLINE_OR_BOOTCONFIG
#define CMD_SUSFS_SET_CMDLINE_OR_BOOTCONFIG 0x555b0
#endif
#ifndef CMD_SUSFS_ADD_OPEN_REDIRECT
#define CMD_SUSFS_ADD_OPEN_REDIRECT 0x555c0
#endif

/* Missing struct types */
struct st_susfs_sus_map {
    char                                    target_pathname[SUSFS_MAX_LEN_PATHNAME];
    int                                     err;
};

struct st_susfs_avc_log_spoofing {
    bool                                    enabled;
    int                                     err;
};

struct st_susfs_enabled_features {
    char                                    enabled_features[8192];
    int                                     err;
};

struct st_susfs_variant {
    char                                    susfs_variant[16];
    int                                     err;
};

struct st_susfs_version {
    char                                    susfs_version[16];
    int                                     err;
};

/* Missing function declarations - these are v2.0.0-only APIs not in susfs4ksu */
extern void susfs_start_sdcard_monitor_fn(void);
extern int susfs_set_hide_sus_mnts_for_non_su_procs(void __user **user_info);
extern int susfs_add_sus_path_loop(void __user **user_info);
extern int susfs_add_sus_map(void __user **user_info);
extern int susfs_set_avc_log_spoofing(void __user **user_info);
extern int susfs_get_enabled_features(void __user **user_info);
extern int susfs_show_variant(void __user **user_info);
extern int susfs_show_version(void __user **user_info);
extern int susfs_starts_with(const char *str, const char *prefix);
extern int susfs_ends_with(const char *str, const char *suffix);
extern bool susfs_is_current_proc_umounted(void);
extern void susfs_set_current_proc_umounted(void);

#endif
