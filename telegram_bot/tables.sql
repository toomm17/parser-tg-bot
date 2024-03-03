create table if not exists users (
    telegram_id bigint primary key,
    username varchar(255) not null,
    created_at timestamp default current_timestamp not null,
    balance integer default 0
);
