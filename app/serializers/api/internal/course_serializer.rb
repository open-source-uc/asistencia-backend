class Api::Internal::CourseSerializer < ActiveModel::Serializer
  type :course

  attributes(
    :id,
    :name,
    :enabled,
    :created_at,
    :updated_at,
    :slug
  )
end
