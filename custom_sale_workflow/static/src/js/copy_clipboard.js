/** @odoo-module **/

import { registry } from "@web/core/registry";
import { CharField } from "@web/views/fields/char/char_field";

const ClipboardCharField = {
    ...CharField,
    name: "clipboard_char",
    template: "ClipboardCharField",
    events: {
        ...CharField.events,
        "click .o_clipboard_button": "_onCopyClick",
    },
    _onCopyClick() {
        navigator.clipboard.writeText(this.props.value).then(() => {
            this.notify({ message: "Copied to clipboard!", type: "success" });
        });
    },
};

registry.category("fields").add("clipboard_char", ClipboardCharField);
