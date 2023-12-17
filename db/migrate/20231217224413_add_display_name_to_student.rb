class AddDisplayNameToStudent < ActiveRecord::Migration[7.0]
  def change
    add_column :students, :display_name, :string
  end
end
