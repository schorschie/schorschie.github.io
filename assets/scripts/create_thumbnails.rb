#!/usr/bin/env ruby
# ruby create_thumbnails.rb path

require 'mini_magick'

MAX_SIDE = 200.0

argument = ARGV[0].dup
path = argument.gsub!("\\", "/")
path = path + "/*.{jpg,png,gif}"

Dir.glob(path) do |image|
    puts "Wroking on #{image}"
    thumbname = File.dirname(image) + "/" +
                File.basename(image, ".*") +
                "_thumb" + File.extname(image)

    image_data = MiniMagick::Image.open(image)
    relative_change = MAX_SIDE / image_data.dimensions.max * 100
    str_rel_change = relative_change.to_s + "%"
    image_data.resize str_rel_change
    image_data.write(thumbname)

    puts "#{thumbname} written."
end
