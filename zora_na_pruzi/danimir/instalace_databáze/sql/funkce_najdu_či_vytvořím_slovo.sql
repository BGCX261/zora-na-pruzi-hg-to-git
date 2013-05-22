-- Function: najdu_či_vytvořím_slovo(character varying)

-- DROP FUNCTION najdu_či_vytvořím_slovo(character varying);

CREATE OR REPLACE FUNCTION najdu_či_vytvořím_slovo(_slovo character varying)
  RETURNS bigint AS
$BODY$

	DECLARE

		_id bigint;
		
	BEGIN
	  
	    SELECT INTO _id "lexikon"."id" FROM "pruga"."lexikon" WHERE "lexikon"."slovo" LIKE "_slovo";
	      
	    IF NOT FOUND THEN
        
            INSERT INTO "pruga"."katalog" ("id_třídy", "kategorie") VALUES(
                                    (SELECT "davaj_id_třídy"('str',  '__builtins__'))
                                    , 'slovo');
            SELECT INTO _id currval('"pruga"."sled_uzlů"'::regclass);
            
			INSERT INTO "pruga"."lexikon" ("id", "slovo") VALUES(_id, "_slovo");
	    END IF;
	      
	    RETURN _id;
	 
	END;
$BODY$
  LANGUAGE plpgsql VOLATILE SECURITY DEFINER
  COST 100;
ALTER FUNCTION najdu_či_vytvořím_slovo(character varying)
  OWNER TO postgres;
COMMENT ON FUNCTION najdu_či_vytvořím_slovo(character varying) IS 'Tato funkce vrátí id z tabulky všech jestvujících slov';
