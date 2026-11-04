alter table products add column if not exists image_url2 text;
alter table products add column if not exists image_url3 text;
alter table products add column if not exists video_url text;
alter table products add column if not exists rating float default 5.0;

create table if not exists live_comments (
  id uuid default gen_random_uuid() primary key,
  live_phone text,
  sender_phone text,
  message text,
  created_at timestamp default now()
);
alter table live_comments enable row level security;
drop policy if exists "public" on live_comments;
create policy "public" on live_comments for all using (true) with check (true);
