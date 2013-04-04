-- Function: "vytvořím_nový_uzel"(character varying, character varying)

-- DROP FUNCTION "vytvořím_nový_uzel"(character varying, character varying);

CREATE OR REPLACE FUNCTION "vytvořím_nový_uzel"("KLÍČ" character varying)
  RETURNS bigint AS
$BODY$

	DECLARE

		_id bigint;
		
	BEGIN
	  
      SELECT INTO _id "klíče"."id" FROM "pruga"."klíče" WHERE "klíče"."klíč" LIKE "KLÍČ" ;
	      
	    IF NOT FOUND THEN
			--INSERT INTO "pruga"."třídy" ("třída", "modul") VALUES("_jméno_třídy", "_jméno_modulu");
			--SELECT INTO _id "třídy"."id" FROM "pruga"."třídy" WHERE "třídy"."třída" LIKE "_jméno_třídy" AND "třídy"."modul" LIKE "_jméno_modulu";
	    END IF;

		INSERT INTO "pruga"."uzly" ("klíč") VALUES(_id);

		SELECT INTO _id currval('"pruga"."uzly_id_seq"'::regclass);
	      
	    RETURN _id;
	 
	END;
$BODY$
  LANGUAGE plpgsql VOLATILE SECURITY DEFINER
  COST 100;
ALTER FUNCTION "vytvořím_nový_uzel"(character varying)
  OWNER TO postgres;
