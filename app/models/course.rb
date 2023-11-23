class Course < ApplicationRecord
  resourcify
  extend FriendlyId
  friendly_id :slug, use: :slugged

  has_many :students, dependent: :destroy
  has_many :activities, dependent: :destroy

  validates :name,
            presence: true

  def users
    User.with_roles(CourseRoles.all, self)
  end
end

# == Schema Information
#
# Table name: courses
#
#  id         :bigint(8)        not null, primary key
#  name       :string           not null
#  enabled    :string           default("t"), not null
#  created_at :datetime         not null
#  updated_at :datetime         not null
#  slug       :string
#
# Indexes
#
#  index_courses_on_slug  (slug) UNIQUE
#
