-- Function: "najdu_či_vytvořím_klíč"(character varying, character varying)

-- DROP FUNCTION "najdu_či_vytvořím_klíč"(character varying, character varying);

CREATE OR REPLACE FUNCTION "davaj_slovo"("ID" bigint)
  RETURNS character varying AS
$BODY$

	DECLARE

		_slovo character varying;
		
	BEGIN
	  
      SELECT INTO _slovo "pruga"."slova"."slovo" FROM "pruga"."slova", "pruga"."uzly" WHERE "pruga"."uzly"."id" = "ID" AND "pruga"."slova"."id" = "pruga"."uzly"."id";
	      
	    --IF NOT FOUND THEN
            --INSERT INTO "pruga"."klíče" ("klíč", "tabulka_hodnot") VALUES("KLÍČ", "TABULKA");
            --SELECT INTO _id currval('"pruga"."klíče_id_seq"'::regclass);
	    --END IF;

	    RETURN _slovo;
	 
	END;
$BODY$
  LANGUAGE plpgsql VOLATILE SECURITY DEFINER
  COST 100;
ALTER FUNCTION "davaj_slovo"(bigint)
  OWNER TO postgres;
