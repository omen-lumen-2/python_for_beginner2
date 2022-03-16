# -*- coding: utf-8 -*-
from model.сontact import Contact


def test_delete_contact(app):
    app.contact.contact_must_exist()
    old_contacts = app.contact.get_contact_list()
    app.contact.delete_first_contact()
    assert len(old_contacts) - 1 == app.contact.get_count_contact()
    new_contacts = app.contact.get_contact_list()
    del old_contacts[0]
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
