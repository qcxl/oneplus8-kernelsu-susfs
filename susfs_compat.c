#include <linux/module.h>
#include <linux/susfs_compat.h>

/* Stub implementations for v2.0.0-only APIs not present in susfs4ksu v1.5.5 */
void susfs_start_sdcard_monitor_fn(void) {}
int susfs_set_hide_sus_mnts_for_non_su_procs(void __user **user_info) { return 0; }
int susfs_add_sus_path_loop(void __user **user_info) { return 0; }
int susfs_add_sus_map(void __user **user_info) { return 0; }
int susfs_set_avc_log_spoofing(void __user **user_info) { return 0; }
int susfs_get_enabled_features(void __user **user_info) { return 0; }
int susfs_show_variant(void __user **user_info) { return 0; }
int susfs_show_version(void __user **user_info) { return 0; }
int susfs_starts_with(const char *str, const char *prefix) { return 0; }
int susfs_ends_with(const char *str, const char *suffix) { return 0; }
bool susfs_is_current_proc_umounted(void) { return false; }
void susfs_set_current_proc_umounted(void) {}
bool susfs_is_allow_su(void) { return true; }
void ksu_escape_to_root(void) {}
struct work_struct susfs_extra_works;
void ksu_selinux_hide_handle_second_stage(void) {}
void ksu_selinux_hide_handle_post_fs_data(void) {}
