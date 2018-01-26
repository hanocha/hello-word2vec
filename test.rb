require 'csv'

arr = CSV.read("taxonomy-with-ids.csv")
first_cats = []

arr.each_with_index do |cat, i|
  next if i == 0
  tmp_cat = cat[1].split(/\s&\s|,\s/)
  tmp_cat.each do |spl_cat|
    spl_cat = spl_cat.tr(' ', '_')
    first_cats << spl_cat unless first_cats.include?(spl_cat) 
  end
end

p first_cats
