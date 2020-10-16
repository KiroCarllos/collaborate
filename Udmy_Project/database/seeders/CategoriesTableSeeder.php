<?php

namespace Database\Seeders;

use App\Models\Category;
use Illuminate\Database\Seeder;

class CategoriesTableSeeder extends Seeder
{
    public function run()
    {
        Category::create(['name' => 'computers']);
        Category::create(['name' => 'accessories']);
        Category::create(['name' => 'gifts']);
    }
}
