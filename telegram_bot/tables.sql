create table if not exists users (
    telegram_id bigint primary key,
    username varchar(255) not null,
    created_at timestamp default current_timestamp not null,
    balance integer default 0
);

create table if not exists sub_plan (
    id integer primary key,
    months_count tinyint not null,
    price_in_usdt integer not null -- maybe numeric
);

-- Sub Plans
INSERT INTO sub_plan (months_count, price_in_usdt) VALUES
    (1, 500),
    (6, 2000),
    (12, 5000)
;
--

create table if not exists subscribers (
    id integer primary key,
    start_sub timestamp default current_timestamp not null,
    end_sub timestamp not null,
    renewal_count integer default 0 not null,
    telegram_id bigint not null,

    -- settings_id integer not null

    foreign key(telegram_id) references users(telegram_id)

    check (start_sub < end_sub)
);

create table if not exists transactions (
    id integer primary key,
    t_hash varchar(255) not null,
    telegram_id bigint not null,

    foreign key(telegram_id) references users(telegram_id)
    unique(t_hash)
);

create table if not exists sub_settings (
    id int primary key
    -- idk next steps
);

