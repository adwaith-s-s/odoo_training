odoo.define('pos_customized.receipt', function(require){
"use strict";

    var models = require('point_of_sale.models');

    models.load_fields('product.product', 'product_owner');
    models.load_fields('product.product', 'rating');

    var _super_orderline = models.Orderline.prototype;
    models.Orderline = models.Orderline.extend({
        export_for_printing: function(){
            var line = _super_orderline.export_for_printing.apply(this, arguments);
            line.product_owner = this.get_product().product_owner;
            line.product_rating = this.get_product().rating;
            console.log("LIne", line.product_rating);
            console.log("owner", line.product_owner[1]);
            return line;
        },
    });

});


