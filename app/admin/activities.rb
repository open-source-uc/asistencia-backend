ActiveAdmin.register Activity do
  permit_params :name, :course_id, :description, :date

  index do
    selectable_column
    id_column
    column :course
    column :name
  end

  show do
    attributes_table do
      row :course
      row :name
      row :description
      row :date
    end
  end

  form do |f|
    f.inputs do
      f.input :course
      f.input :name
      f.input :description
      f.input :date
    end
    f.actions
  end
end
