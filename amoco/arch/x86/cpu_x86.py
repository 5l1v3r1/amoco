# -*- coding: utf-8 -*-

from amoco.arch.x86.asm import *
# expose "microarchitecture" (instructions semantics)
uarch = dict(filter(lambda kv:kv[0].startswith('i_'),locals().items()))

from amoco.arch.core import instruction, disassembler

instruction_x86 = type('instruction_x86',(instruction,),{})
instruction_x86.set_uarch(uarch)

from amoco.arch.x86.formats import *

from amoco.arch.x86 import spec_ia32
disassemble = disassembler([spec_ia32],iclass=instruction_x86)
disassemble.maxlen = 15

def PC():
    return eip

def configure(**kargs):
    from amoco.config import get_module_conf
    conf = get_module_conf('x86')
    conf.update(kargs)
    # asm format:
    if conf['format'] in ('AT&T','at&t','ATT','att'):
        instruction_x86.set_formatter(IA32_ATT)
    else:
        instruction_x86.set_formatter(IA32_Intel)

configure()
