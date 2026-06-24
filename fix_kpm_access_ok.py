import re
p = 'drivers/kernelsu/kpm/kpm.c'
t = open(p).read()
t = t.replace(
    '#include "compact.h"',
    '#include "compact.h"\n#if LINUX_VERSION_CODE < KERNEL_VERSION(5,0,0)\n#undef access_ok\n#define access_ok(addr, size) __range_ok(addr, size)\n#endif'
)
open(p, 'w').write(t)
print('Patched kpm.c for access_ok compatibility')
