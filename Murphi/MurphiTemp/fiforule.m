# $0$ fifobuffer
# $1$ OBJSET_directory
# $2$ directory
# $3$ cache

ruleset n:Machines do
  alias p:$0$[n] do

      rule "$0$"
        (p.QueueInd>0)
      ==>
        alias msg:p.Queue[0] do
          if IsMember(n, $1$) then
            if Func_$2$(msg, n) then
              PopQueue($0$, n);
            endif;
          else
            if Func_$3$(msg, n) then
              PopQueue($0$, n);
            endif;
          endif;
        endalias;

      endrule;
  endalias;
endruleset;