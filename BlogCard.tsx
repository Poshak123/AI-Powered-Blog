interface Props {
  title: string;
  content: string;
}

export default function BlogCard({ title, content }: Props) {
  return (
    <div style={{ border: "1px solid #ccc", padding: "1rem", marginBottom: "1rem" }}>
      <h3>{title}</h3>
      <p>{content}</p>
    </div>
  );
}
