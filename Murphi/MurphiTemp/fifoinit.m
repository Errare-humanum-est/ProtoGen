# $0$ fifoname

for i:Machines do
    undefine $0$[i].Queue;
    $0$[i].QueueInd:=0;
endfor;