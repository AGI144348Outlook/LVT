-- Elemental Vault v0: apply only to a dedicated isolated Neon database.
-- Generator tables contain no empirical element reference answers.
CREATE SCHEMA IF NOT EXISTS elemental_vault;
CREATE TABLE IF NOT EXISTS elemental_vault.seed (
    seed_id BIGINT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    name TEXT NOT NULL UNIQUE,
    atomic_number INTEGER NOT NULL CHECK (atomic_number > 0),
    protons INTEGER NOT NULL CHECK (protons > 0),
    neutrons INTEGER NOT NULL CHECK (neutrons >= 0),
    electrons INTEGER NOT NULL CHECK (electrons >= 0),
    provenance TEXT NOT NULL
);
CREATE TABLE IF NOT EXISTS elemental_vault.experiment (
    experiment_id BIGINT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    created_at TIMESTAMPTZ NOT NULL DEFAULT now(),
    engine_version TEXT NOT NULL,
    laws_version TEXT NOT NULL,
    inputs JSONB NOT NULL,
    notes TEXT
);
CREATE TABLE IF NOT EXISTS elemental_vault.candidate (
    candidate_id BIGINT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    experiment_id BIGINT NOT NULL REFERENCES elemental_vault.experiment,
    protons INTEGER NOT NULL CHECK (protons > 0),
    neutrons INTEGER NOT NULL CHECK (neutrons >= 0),
    candidate_status TEXT NOT NULL DEFAULT 'unvalidated_candidate',
    derivation JSONB NOT NULL,
    UNIQUE (experiment_id, protons, neutrons)
);
INSERT INTO elemental_vault.seed (name, atomic_number, protons, neutrons, electrons, provenance)
VALUES ('hydrogen-1', 1, 1, 0, 1, 'Hydrogen-1 seed; measured values and law provenance must be pinned before scientific runs')
ON CONFLICT (name) DO NOTHING;
