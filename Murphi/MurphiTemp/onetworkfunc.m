# $0$ networkname
# $1$ cnt+networkname
# $2$ networkmax

procedure Send_$0$(msg:Message);
  Assert($1$[msg.dst] < $2$) "Too many messages";
  $0$[msg.dst][$1$[msg.dst]] := msg;
  $1$[msg.dst] := $1$[msg.dst] + 1;
end;

procedure Pop_$0$(n:Machines);
begin
  Assert ($1$[n] > 0) "Trying to advance empty Q";
  for i := 0 to $1$[n]-1 do
    if i < $1$[n]-1 then
      $0$[n][i] := $0$[n][i+1];
    else
      undefine $0$[n][i];
    endif;
  endfor;
  $1$[n] := $1$[n] - 1;
end;