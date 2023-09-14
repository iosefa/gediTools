CREATE TABLE IF NOT EXISTS ancillary_table
                (
                    dz double precision,
                    l2a_alg_count integer,
                    maxheight_cuttoff double precision,
                    rg_eg_constraint_center_buffer integer,
                    rg_eg_mpfit_max_func_evals smallint,
                    rg_eg_mpfit_maxiters smallint,
                    rg_eg_mpfit_tolerance double precision,
                    signal_search_buff double precision,
                    tx_noise_stddev_multiplier double precision,
                    orbit_number integer NOT NULL,
                    sub_orbit_number smallint NOT NULL,
                    PRIMARY KEY (orbit_number, sub_orbit_number)
                );