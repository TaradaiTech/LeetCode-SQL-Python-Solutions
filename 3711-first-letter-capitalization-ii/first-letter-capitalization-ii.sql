-- Use a CTE to split the content into words, format each word, and then reassemble the text.
WITH formatted_content AS (
    SELECT 
        content_id,
        content_text AS original_text,
        -- Reassemble the formatted words into a single string
        STRING_AGG(
            CASE 
                -- Check if the word contains a hyphen
                WHEN word LIKE '%-%' THEN
                    -- For hyphenated words, split by '-', capitalize each part with INITCAP, then join them back with '-'
                    ARRAY_TO_STRING(
                        ARRAY(
                            SELECT INITCAP(part) 
                            FROM UNNEST(string_to_array(word, '-')) AS part
                        ), 
                        '-'
                    )
                ELSE
                    -- For non-hyphenated words, just apply INITCAP to capitalize the first letter and lower the rest.
                    INITCAP(word)
            END, 
            ' '   -- Rejoin the words with a space separator
        ) AS converted_text
    FROM (
        -- Split the content_text into individual words by spaces
        SELECT 
            content_id,
            content_text,
            UNNEST(string_to_array(content_text, ' ')) AS word
        FROM user_content
    ) AS words
    GROUP BY content_id, content_text
)
-- Return both the original and the converted text for each content_id, ordered by content_id.
SELECT content_id, original_text, converted_text
FROM formatted_content
ORDER BY content_id;