# Permissions & Groups Configuration

## Custom Permissions

Defined in `book` model:

- `can_view`: Can view book
- `can_create`: Can create book
- `can_edit`: Can edit book
- `can_delete`: Can delete book

## Groups

- **Viewers**: `can_view`
- **Editors**: `can_view`, `can_create`, `can_edit`
- **Admins**: All permissions

## Setup Steps

1. Defined custom permissions in `book.Meta.permissions`.
2. Created groups and assigned permissions via Django admin.
3. Used `@permission_required` in views to protect actions.
4. User access verified by assigning them to different groups.
5. Templates conditionally render content based on permissions.

## Example

In template:

```django
{% if perms.relationship_app.can_delete %}
    <a href="{% url 'delete_book' book.id %}">Delete</a>
{% endif %}