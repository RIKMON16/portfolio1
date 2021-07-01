# Working in Postgres CMD

## To Delete / Search DB

- Step One:
  - log in as postgres user (my user is called rishipalsingh):
  - `sudo -i -u postgres`

- Step Two:
  - Open an sql terminal and connect to your database:
  - `psql -d database_name(rishipalsingh)`

- Step Three:
  - List your table and spot the tables related to that app:
  - \dt;

- Step Four:
  - Drop them (consider drop order with relations):
  - `DROP TABLE tablename ;` drop stands for delete

- Step Five:
  - List migration record, you will see migrations applied classified like so:
  - id | app | name | applied

## `SELECT * FROM django_migrations;`

- Delete rows of migrations of that app (you can delete by id or by app, with app don't forget 'quotes'):

- DELETE FROM django_migrations WHERE app='yourapp';

- log out and run your migrations merely (maybe run makemigrations in your case):

- python manage.py migrate --settings=your.settings.module_if_any

Note: it is possible that in your case will not have to drop all the tables of that app and not all the migrations, just the ones of the models causing the problem.
