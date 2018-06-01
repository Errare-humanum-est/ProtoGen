# $0$ archname
# $1$ machineset
# $2$ maxindex

procedure $0$_Defermsg(msg:Message; adr: Address; m:$1$);
begin
	alias cle: $0$[m].CL[adr] do
	alias q: cle.Defermsg.Queue do
	alias qind: cle.Defermsg.QueueInd do

	if (qind<=$2$) then
      q[qind]:=msg;
      qind:=qind+1;
    endif;

	endalias;
	endalias;
	endalias;
end;

procedure $0$_SendDefermsg(adr: Address; m:$1$);
begin
  alias cle: $0$[m].CL[adr] do
  alias q: cle.Defermsg.Queue do
  alias qind: cle.Defermsg.QueueInd do

  for i := 0 to qind-1 do
  		--$0$_Updatemsg(q[i], adr, m);
  		Send_resp(q[i]);
        undefine q[i];
    endfor;

   qind := 0;

  endalias;
  endalias;
  endalias;
end;

