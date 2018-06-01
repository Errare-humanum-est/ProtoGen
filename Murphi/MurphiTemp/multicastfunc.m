# $0$ networkname
# $1$ Vector for multicast

procedure Multicast_$0$_$1$(var msg: Message; dst:$1$;);
begin
      for iSV:Machines do
          if iSV!=msg.src then
            if MultiSetCount(i:dst, dst[i] = iSV) = 1 then
              msg.dst := iSV;
              Send_$0$(msg);
            endif;
          endif;
      endfor;
end;