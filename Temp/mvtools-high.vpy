##SOURCE_https://gist.github.com/KCCat/1b3a7b7f085a066af3719859f88ded02
##极高消耗，建议线程数高于16的高端处理器使用此脚本进行补帧测试。

import vapoursynth as vs
core = vs.core

vfps = int(container_fps*1e3)
vden = 1e3

if not (container_fps > 32):

    input = video_in

    cut = core.std.AssumeFPS(
                             clip=input, fpsnum=vfps, fpsden=vden
                             )

    sup  = core.mv.Super(
                         clip=cut, pel=2, sharp=2, rfilter=4,
                         hpad=16, vpad=8, levels=0
                         )

    bvec = core.mv.Analyse(
                           super=sup, blksize=32, blksizev=16, overlap=16,
                           overlapv=8, levels=0, isb=True, search=3,
                           searchparam=0, pelsearch=3, badrange=-1, badsad=10000
                           )

    fvec = core.mv.Analyse(
                           super=sup, blksize=32, blksizev=16,
                           overlap=16, overlapv=8, levels=0, isb=False,
                           search=3, searchparam=0, pelsearch=3,
                           badrange=-1, badsad=10000
                           )

    output = core.mv.BlockFPS(
                              clip=cut, super=sup, mvbw=bvec, mvfw=fvec,
                              num=60, den=1, mode=2, ml=1020.0,
                              thscd1=16320, thscd2=255
                              )

    output.set_output()
