# $0$ networkname
# $1$ networkmax

procedure Send_$0$(msg:Message;);
  Assert (MultiSetCount(i:$0$[msg.dst], true) < $1$) "Too many messages";
  MultiSetAdd(msg, $0$[msg.dst]);
end;