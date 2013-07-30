MATCH t:`Účtová třída`-[ms:`MÁ SKUPINU`]->s:`Účtová skupina`-[mu:`MÁ ÚČET`]->u:`Účet`
RETURN t,s,u,ms,mu;

MATCH n-[r:`MÁ SKUPINU`|`MÁ ÚČET`]->m RETURN ID(n) AS z_id, ID(m) AS do_id;
