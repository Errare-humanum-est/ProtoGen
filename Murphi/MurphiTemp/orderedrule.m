# $0$ networkname
# $1$ cnt_network
# $2$ buf_networkname
# $3$ OBJSET_directory
# $4$ directory
# $5$ cache

ruleset n:Machines do
    alias msg:$0$[n][0] do
      rule "Receive $0$"
        $1$[n] > 0
      ==>
        -- With input queues
        if (ENABLE_QS) then
          if PushQueue($2$, n, msg) then
            Pop_$0$(n);
          endif;
        else
        -- Without input queues
          if IsMember(n, $3$) then
            if Func_$4$(msg, n) then
              Pop_$0$(n);
            endif;
          else
            if Func_$5$(msg, n) then
              Pop_$0$(n);
            endif;
          endif;
        endif;
      endrule;
    endalias;

endruleset;