-- Table: pruga.uzly

-- DROP TABLE "pruga"."uzly";

CREATE TABLE "pruga"."uzly"
(
  "id" bigserial NOT NULL,
  "klíč" bigint NOT NULL,
  CONSTRAINT "uzly_pkey" PRIMARY KEY ("id"),
  CONSTRAINT "uzly_klíč_fkey" FOREIGN KEY ("klíč")
      REFERENCES "pruga"."klíče" ("id") MATCH SIMPLE
      ON UPDATE NO ACTION ON DELETE NO ACTION
)
WITH (
  OIDS=FALSE
);
ALTER TABLE "pruga"."uzly"
  OWNER TO postgres;
