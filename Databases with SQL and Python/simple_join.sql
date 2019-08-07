-- Find the names of the individual animals that eat fish.
--
-- The animals table has columns (name, species, birthdate) for each individual.
-- The diet table has columns (species, food) for each food that a species eats.

--select animals.name, animals.species, diet.food
--from animals join diet --joins tables 'animals' and 'diet'
--on animals.species = diet.species --joins the two tables where species is the same!
--limit 10; --limit the number of results to 10

--Return only the names of the animals that eat fish
--select animals.name
--from animals join diet
--on animals.species = diet.species
--where diet.food = 'fish'
--limit 100

--Same query, but using the simple join without the 'join' command
select animals.name
from animals, diet
where animals.species = diet.species
and diet.food = 'fish'
limit 100

-- List all the taxonomic orders, using their common names, sorted by the
-- number of animals of that order that the zoo has.
--
-- The animals table has (name, species, birthdate) for each individual.
-- The taxonomy table has (name, species, genus, family, t_order) for each species.
-- The ordernames table has (t_order, name) for each order.
--
-- Be careful:  Each of these tables has a column "name", but they don't
-- have the same meaning!  animals.name is an animal's individual name.
-- taxonomy.name is a species' common name (like 'brown bear').
-- And ordernames.name is the common name of an order (like 'Carnivores').

-- We can join more than two tables to get a result!

select ordernames.name, count(*) as num
  from animals, taxonomy, ordernames
  where animals.species = taxonomy.name
    and taxonomy.t_order = ordernames.t_order
  group by ordernames.name
  order by num desc

-----------------------------------
-- Practice with where vs. having --
-- where comes before the aggregation, and having comes after! --

-- Find the one food that is eaten by only one animal.
--
-- The animals table has columns (name, species, birthdate) for each
-- individual.
-- The diet table has columns (species, food) for each food that a
-- species eats.

select diet.food, diet.species, animals.name, count(food) as number_of_eaters
from animals, diet
where animals.species = diet.species
group by food
having number_of_eaters = 1;
