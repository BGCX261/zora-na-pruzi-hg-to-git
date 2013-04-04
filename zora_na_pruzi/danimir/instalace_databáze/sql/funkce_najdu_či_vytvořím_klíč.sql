-- Function: "najdu_či_vytvořím_klíč"(character varying, character varying)

-- DROP FUNCTION "najdu_či_vytvořím_klíč"(character varying, character varying);

CREATE OR REPLACE FUNCTION "najdu_či_vytvořím_klíč"("KLÍČ" character varying, "TABULKA" character varying)
  RETURNS bigint AS
$BODY$

	DECLARE

		_id bigint;
		
	BEGIN
	  
      SELECT INTO _id "klíče"."id" FROM "pruga"."klíče" WHERE "klíče"."klíč" LIKE "KLÍČ" ;
	      
	    IF NOT FOUND THEN
            INSERT INTO "pruga"."klíče" ("klíč", "tabulka_hodnot") VALUES("KLÍČ", "TABULKA");
            SELECT INTO _id currval('"pruga"."klíče_id_seq"'::regclass);
	    END IF;

	    RETURN _id;
	 
	END;
$BODY$
  LANGUAGE plpgsql VOLATILE SECURITY DEFINER
  COST 100;
ALTER FUNCTION "najdu_či_vytvořím_klíč"(character varying, character varying)
  OWNER TO postgres;
