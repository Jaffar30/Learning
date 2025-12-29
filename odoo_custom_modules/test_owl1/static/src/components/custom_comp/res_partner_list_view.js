/** @odoo-module **/

import { registry } from "@web/core/registry";
import { ListView } from "@web/views/list/list_view";
import { ListController } from "@web/views/list/list_controller";

class ResPartnerListController extends ListController {
    setup() {
        super.setup();
        console.log("inherit worked");
    }
}

export const ResPartnerListView = {
    ...ListView,
    Controller: ResPartnerListController,
};

registry.category("views").add("res_partner_list_controller", ResPartnerListView);
