-- Table: pruga.lexikon

-- DROP TABLE "pruga"."slova";

CREATE TABLE "pruga"."slova"
(
  "id" bigint NOT NULL,
  "slovo" character varying(255) NOT NULL,
  CONSTRAINT "pk_slova" PRIMARY KEY ("id"),
  CONSTRAINT "slova_uzly_fkey" FOREIGN KEY ("id")
      REFERENCES "pruga"."uzly" ("id") MATCH SIMPLE
      ON UPDATE NO ACTION ON DELETE CASCADE
)
WITH (
  OIDS=FALSE
);
ALTER TABLE "pruga"."slova"
  OWNER TO postgres;
