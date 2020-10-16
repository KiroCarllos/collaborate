<?php

namespace App\Http\Controllers;

use App\Models\Category;
use App\Models\Product;
use App\Models\Tag;
use Illuminate\Http\Request;

class EcommerceController extends Controller
{
    public function index(Request $request)
    {
        $keyword = $request->has('keyword') ? $request->keyword : null;
        $selected_price = $request->has('price') ? $request->get('price') : null;
        $selected_category = $request->has('category') ? $request->get('category') : null;
        $selected_tags = $request->has('tags') ? $request->get('tags') : [];


        $categories= Category::all();
        $tags = Tag::all();


        $products = Product::with(['category','tags']);
        if ($keyword != null){
            $products = $products->search($keyword);
        }
        if ($selected_price != null) {
            $products = $products->when($selected_price, function ($query) use ($selected_price){
                if ($selected_price == 'price_0_500') {
                    $query->whereBetween('price', [0, 500]);
                } elseif ($selected_price == 'price_501_1500') {
                    $query->whereBetween('price', [501, 1500]);
                } elseif ($selected_price == 'price_1501_3000') {
                    $query->whereBetween('price', [1501, 3000]);
                } elseif ($selected_price == 'price_3001_5000') {
                    $query->whereBetween('price', [3001, 5000]);
                }
            });
        }

        if ($selected_category != null) {
            $products = $products->whereCategoryId($selected_category);
        }

        if (is_array($selected_tags) && count($selected_tags) > 0) {
            $products = $products->whereHas('tags', function ($query) use ($selected_tags) {
                $query->whereIn('product_tag.tag_id', $selected_tags);
            });
        }

        $products =$products->orderByDesc('id')->simplePaginate(6);

        return view('frontend.index', compact('products', 'categories', 'tags', 'keyword', 'selected_price', 'selected_category', 'selected_tags'));
    }
}
