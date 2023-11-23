class Api::Internal::ActivitySerializer < ActiveModel::Serializer
  type :activity

  attributes(
    :id,
    :course_id,
    :name_ciphertext,
    :description_ciphertext,
    :date,
    :created_at,
    :updated_at,
    :slug
  )
end
