class Activity < ApplicationRecord
  extend FriendlyId
  friendly_id :slug, use: :slugged

  belongs_to :course
  has_many :attendances, dependent: :destroy

  has_encrypted :name, :description
end

# == Schema Information
#
# Table name: activities
#
#  id                     :bigint(8)        not null, primary key
#  course_id              :bigint(8)        not null
#  name_ciphertext        :string           not null
#  description_ciphertext :string           not null
#  date                   :date
#  created_at             :datetime         not null
#  updated_at             :datetime         not null
#  slug                   :string
#
# Indexes
#
#  index_activities_on_course_id  (course_id)
#  index_activities_on_slug       (slug) UNIQUE
#
# Foreign Keys
#
#  fk_rails_...  (course_id => courses.id)
#
