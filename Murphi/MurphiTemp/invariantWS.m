# $0$ Obj_Machine
# $1$ Address
# $2$ Perm
# $3$ Machine
# $4$ CL
# $5$ Access
# $6$ Permission

invariant "Write Serialization"
    forall c1:$0$ do
    forall c2:$0$ do
    forall a:$1$ do
    ( c1 != c2
    & $3$[c1].$4$[a].$5$ = $6$ )
    ->
    ( $3$[c2].$4$[a].$5$ != $6$ )
    endforall
    endforall
    endforall;
