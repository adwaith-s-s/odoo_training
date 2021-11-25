odoo.define('pos_customized.pos_order_line', function(require) {
"use strict";

var models = require('point_of_sale.models');



models.Orderline = models.Orderline.extend({

    get_product_owner: function(){
        const product = this.product;
        console.log(this.product.product_owner)
        return this.product.product_owner[1];
    },

});

});
