using UnityEngine;

namespace com.github.lhervier.ksp.fix.terrainprecision
{
    /// <summary>
    /// What the fixes of the scatter (<see cref="ScatterFix"/>) and of the surface features
    /// (<see cref="RocFix"/>) share: stock places the holders of both the same way, under the terrain sphere at
    /// the 600 km position of their quad.
    /// </summary>
    internal static class Utils
    {
        /// <summary>
        /// Whether a holder hung from this quad, at no offset, is drawn with the very matrix the quad is: true
        /// when the quad's own transform holds no 600 km vector.
        /// </summary>
        public static bool CanHangFrom(PQ quad)
        {
            if (quad == null)
            {
                return false;
            }
            PQS sphere = quad.sphereRoot;

            // On a sphere whose quads are not surface relative, stock places the holder at the centre of the
            // body, not at a 600 km vector: nothing to fix there.
            if (sphere == null || !sphere.surfaceRelativeQuads || sphere.LocalSpacePQStorage == null)
            {
                return false;
            }

            // For BurstPQS: on the bodies it builds, a quad is drawn with its own transform wherever it hangs,
            // and its holder can hang from it whatever its parent. See BurstPQSCompat.
            if (BurstPQSCompat.PlacesTerrain(sphere))
            {
                return true;
            }

            // Only the quads of the highest subdivision level are moved to this storage, which is not attached
            // to the body, and they are the only ones stock gives scatter and surface features to. Any other
            // quad hangs from the sphere itself, with the same kind of 600 km local position as the holder, so
            // hanging the holder from it would gain nothing.
            return quad.transform.parent == sphere.LocalSpacePQStorage.transform;
        }

        /// <summary>
        /// How far above the quad Unity draws the holder, in millimetres, along the vertical of the quad.
        /// Negative when the holder is drawn below it.
        /// </summary>
        public static double DrawnOffsetMm(Transform holder, PQ quad)
        {
            // Both are drawn with their local to world matrix. Its translation is a world position, so near
            // the floating origin, and the difference of two of them is short: a double holds it exactly.
            Vector3d holderOrigin = (Vector3)holder.localToWorldMatrix.GetColumn(3);
            Vector3d quadOrigin = (Vector3)quad.transform.localToWorldMatrix.GetColumn(3);

            // The vertical at the quad: the direction of its origin from the centre of the body, a unit
            // vector in the sphere's frame, turned into world axes. No long vector involved, and a float
            // direction is far more precise than needed on a gap of a few centimetres.
            Vector3d up = ((Vector3d)quad.sphereRoot.transform.TransformDirection(
                (Vector3)quad.positionPlanetRelative)).normalized;

            return Vector3d.Dot(holderOrigin - quadOrigin, up) * 1000.0;
        }
    }
}
