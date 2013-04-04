-- Table: pruga."klíče"

-- DROP TABLE pruga."klíče";

CREATE TABLE "pruga"."klíče"
(
  "id bigint" NOT NULL DEFAULT nextval('"pruga"."klíče_id_seq"'::regclass),
  "klíč" character varying,
  "tabulka_hodnot" character varying,
  CONSTRAINT "klíče_pkey" PRIMARY KEY ("id"),
  CONSTRAINT "klíče_klíč_key" UNIQUE ("klíč" )
)
WITH (
  OIDS=FALSE
);
ALTER TABLE "pruga"."klíče"
  OWNER TO postgres;
