/** @odoo-module */

import { Component, useState } from "@odoo/owl";

export class MyOwlComponent extends Component {
    setup() {
        // Initialize state for the component
        this.state = useState({
            count: this.props.initialCount || 0,
            message: this.props.message || "Hello, OWL!",
        });
    }

    // Event handler to increment the count
    _incrementCount() {
        this.state.count++;
    }

    // Static properties for the component
    static template = "my_module.MyOwlComponentTemplate";
    static props = {
        initialCount: { type: Number, optional: true },
        message: { type: String, optional: true },
    };
} 