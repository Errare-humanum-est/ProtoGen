# $0$ networkname
# $1$ cnt_network

undefine $0$;
for n:Machines do
  $1$[n] := 0;
endfor;