# $0$ networkname
# $1$ buf_networkname
# $2$ OBJSET_directory
# $3$ directory
# $4$ cache

ruleset n:Machines do

    choose midx:$0$[n] do
        alias mach:$0$[n] do
        alias msg:mach[midx] do
          rule "Receive $0$"
            !isundefined(msg.mtype)
          ==>
            if (ENABLE_QS) then
              if PushQueue($1$, n, msg) then
                MultiSetRemove(midx, mach);
              endif;
            else
              -- Without input queues
              if IsMember(n, $2$) then
                if Func_$3$(msg, n) then
                  MultiSetRemove(midx, mach);
                endif;
              else
                if Func_$4$(msg, n) then
                  MultiSetRemove(midx, mach);
                endif;
              endif;
            endif;
          endrule;
        endalias;
        endalias;
    endchoose;

endruleset;